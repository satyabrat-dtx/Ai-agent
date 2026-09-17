# DB2ADMIN.TRAVELTRANSACTION

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 28
- **Primary key**: `COMPANYCODE`, `SERIALNO`, `TRAVELTYPE`
- **FK degree**: referenced by 1 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 169291

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `SERIALNO` | BIGINT | NOT NULL | PK | primary_key |  |
| 2 | `TRAVELTYPE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `CONSULTANT` | INTEGER | NOT NULL |  |  |  |
| 4 | `CONSULTANTCODEICSTABLECODE` | CHAR(4) |  | FK | foreign_key |  |
| 5 | `CONSULTANTCODECODE` | CHAR(6) |  | FK | foreign_key |  |
| 6 | `EMPLOYEEIDCODE` | CHAR(9) |  | FK | foreign_key |  |
| 7 | `TOURNUMBER` | BIGINT | NOT NULL |  |  |  |
| 8 | `EMPGRADE` | CHAR(4) |  |  |  |  |
| 9 | `REQUESTDATE` | DATE | NOT NULL |  |  |  |
| 10 | `FROMDATE` | DATE | NOT NULL |  |  | Inclusive start of a validity period. |
| 11 | `TODATE` | DATE | NOT NULL |  |  | End of a validity period. |
| 12 | `ACTTRVFROMDATE` | TIMESTAMP | NOT NULL |  |  |  |
| 13 | `ACTTRVTODATE` | TIMESTAMP | NOT NULL |  |  |  |
| 14 | `TRAVELPURPOSE` | CHAR(100) |  |  |  |  |
| 15 | `ADVANCEREQUESTED` | DECIMAL(17,2) | NOT NULL |  |  |  |
| 16 | `ADVSANCTIONAMT` | DECIMAL(17,2) |  |  |  |  |
| 17 | `ADVANCEAPPROVEDBYCODE` | CHAR(9) |  | FK | foreign_key |  |
| 18 | `TOURAPPROVEDBYCODE` | CHAR(9) |  | FK | foreign_key |  |
| 19 | `REQPENDINGWITH` | CHAR(35) |  |  |  |  |
| 20 | `AUTHLEVEL` | CHAR(10) |  |  |  |  |
| 21 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 22 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 23 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 24 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 25 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 26 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 27 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `TRAVELTRANSACTION.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_ADVANCEAPPROVEDBY` | `COMPANYCODE`, `ADVANCEAPPROVEDBYCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `TRAVELTRANSACTION.COMPANYCODE = EMPLOYEE.COMPANYCODE AND TRAVELTRANSACTION.ADVANCEAPPROVEDBYCODE = EMPLOYEE.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `TRAVELTRANSACTION.COMPANYCODE = EMPLOYEE.COMPANYCODE AND TRAVELTRANSACTION.EMPLOYEEIDCODE = EMPLOYEE.CODE` |
| `EMPLOYEE_TOURAPPROVEDBY` | `COMPANYCODE`, `TOURAPPROVEDBYCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `TRAVELTRANSACTION.COMPANYCODE = EMPLOYEE.COMPANYCODE AND TRAVELTRANSACTION.TOURAPPROVEDBYCODE = EMPLOYEE.CODE` |
| `ICSENTITY_CONSULTANTCODE` | `COMPANYCODE`, `CONSULTANTCODEICSTABLECODE`, `CONSULTANTCODECODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `TRAVELTRANSACTION.COMPANYCODE = ICSENTITY.COMPANYCODE AND TRAVELTRANSACTION.CONSULTANTCODEICSTABLECODE = ICSENTITY.ICSTABLECODE AND TRAVELTRANSACTION.CONSULTANTCODECODE = ICSENTITY.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `TRAVELTRANSACTION_LINE` | [`TRAVELTRANSACTIONDETAIL`](../HR/TRAVELTRANSACTIONDETAIL.md) | `TRAVELTRANSACTIONCOMPANYCODE`, `TRAVELTRANSACTIONSERIALNO`, `TRAVELTRANSACTIONTRAVELTYPE` | `TRAVELTRANSACTIONDETAIL.TRAVELTRANSACTIONCOMPANYCODE = TRAVELTRANSACTION.COMPANYCODE AND TRAVELTRANSACTIONDETAIL.TRAVELTRANSACTIONSERIALNO = TRAVELTRANSACTION.SERIALNO AND TRAVELTRANSACTIONDETAIL.TRAVELTRANSACTIONTRAVELTYPE = TRAVELTRANSACTION.TRAVELTYPE` |

## Indexes

- `TRAVELTRANSACTIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.SERIALNO,
       t.TRAVELTYPE,
       t.CONSULTANT,
       t.CONSULTANTCODEICSTABLECODE,
       t.CONSULTANTCODECODE,
       t.EMPLOYEEIDCODE,
       t.TOURNUMBER,
       t.EMPGRADE,
       t.REQUESTDATE,
       t.FROMDATE,
       t.TODATE
FROM   DB2ADMIN.TRAVELTRANSACTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
