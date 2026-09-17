# DB2ADMIN.TRAVELSETTLEMENT

- **Module**: `HR` (low confidence — FK neighbourhood: 2 of 2 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 30
- **Primary key**: `COMPANYCODE`, `SETTLEMENTNO`, `TOURNUMBERTOURNUMBER`
- **FK degree**: referenced by 1 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 169176

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `SETTLEMENTNO` | BIGINT | NOT NULL | PK | primary_key |  |
| 2 | `TOURNUMBERTOURNUMBER` | BIGINT | NOT NULL | PK | primary_key |  |
| 3 | `TRAVELTYPE` | INTEGER | NOT NULL |  |  |  |
| 4 | `EMPLOYEEID` | CHAR(9) |  |  |  |  |
| 5 | `ADVANCEAMT` | DECIMAL(17,2) | NOT NULL |  |  |  |
| 6 | `TOTALEXPENDITURE` | DECIMAL(17,2) | NOT NULL |  |  |  |
| 7 | `COMPANYSPENT` | DECIMAL(17,2) | NOT NULL |  |  |  |
| 8 | `SELFSPENT` | DECIMAL(17,2) | NOT NULL |  |  |  |
| 9 | `SETTLEMENTAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 10 | `PAIDAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 11 | `REQUESTEDDATE` | DATE | NOT NULL |  |  |  |
| 12 | `TRAVELSTATUS` | CHAR(2) |  |  |  |  |
| 13 | `PAYMENTMODE` | CHAR(1) | NOT NULL |  |  |  |
| 14 | `PROCESSPERIODNOPAYROLLCODE` | CHAR(3) |  | FK | foreign_key |  |
| 15 | `PROCESSPERIODNOPROCESSPERIOD` | INTEGER | NOT NULL | FK | foreign_key |  |
| 16 | `SETTLEMENTDATE` | DATE |  |  |  |  |
| 17 | `APPROVEDDATE` | DATE |  |  |  |  |
| 18 | `APPROVEDBYCODE` | CHAR(9) |  | FK | foreign_key |  |
| 19 | `REQPENDINGWITH` | CHAR(10) |  |  |  |  |
| 20 | `AUTHLEVEL` | CHAR(10) |  |  |  |  |
| 21 | `BANKNAME` | CHAR(15) |  |  |  |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 26 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 27 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 28 | `STEP` | CHAR(1) |  |  |  |  |
| 29 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `TRAVELSETTLEMENT.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_APPROVEDBY` | `COMPANYCODE`, `APPROVEDBYCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `TRAVELSETTLEMENT.COMPANYCODE = EMPLOYEE.COMPANYCODE AND TRAVELSETTLEMENT.APPROVEDBYCODE = EMPLOYEE.CODE` |
| `PAYROLLPROCESSPERIOD_PROCESSPERIODNO` | `COMPANYCODE`, `PROCESSPERIODNOPAYROLLCODE`, `PROCESSPERIODNOPROCESSPERIOD` | [`PAYROLLPROCESSPERIOD`](../HR/PAYROLLPROCESSPERIOD.md) | `COMPANYCODE`, `PAYROLLCODE`, `PROCESSPERIOD` | RESTRICT | `TRAVELSETTLEMENT.COMPANYCODE = PAYROLLPROCESSPERIOD.COMPANYCODE AND TRAVELSETTLEMENT.PROCESSPERIODNOPAYROLLCODE = PAYROLLPROCESSPERIOD.PAYROLLCODE AND TRAVELSETTLEMENT.PROCESSPERIODNOPROCESSPERIOD = PAYROLLPROCESSPERIOD.PROCESSPERIOD` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `TRAVELSETTLEMENT_LINE` | [`TRAVELSETTLEMENTDETAIL`](../HR/TRAVELSETTLEMENTDETAIL.md) | `TRAVELSETTLEMENTCOMPANYCODE`, `TRAVELSETTLEMENTSETTLEMENTNO`, `TSTTOURNUMBERTOURNUMBER` | `TRAVELSETTLEMENTDETAIL.TRAVELSETTLEMENTCOMPANYCODE = TRAVELSETTLEMENT.COMPANYCODE AND TRAVELSETTLEMENTDETAIL.TRAVELSETTLEMENTSETTLEMENTNO = TRAVELSETTLEMENT.SETTLEMENTNO AND TRAVELSETTLEMENTDETAIL.TSTTOURNUMBERTOURNUMBER = TRAVELSETTLEMENT.TOURNUMBERTOURNUMBER` |

## Indexes

- `TRAVELSETTLEMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.SETTLEMENTNO,
       t.TOURNUMBERTOURNUMBER,
       t.TRAVELTYPE,
       t.EMPLOYEEID,
       t.ADVANCEAMT,
       t.TOTALEXPENDITURE,
       t.COMPANYSPENT,
       t.SELFSPENT,
       t.SETTLEMENTAMOUNT,
       t.PAIDAMOUNT,
       t.REQUESTEDDATE
FROM   DB2ADMIN.TRAVELSETTLEMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
