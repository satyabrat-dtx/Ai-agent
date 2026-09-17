# DB2ADMIN.FINLOANPAY

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `LTYPEUSERGENERICGROUPTYPECODE`, `LOANTYPECODE`, `LOANCODELOANNO`, `SCHEDULENO`, `SCHEDULESEQNO`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 223485

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `LTEUGENGROUPTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 2 | `LTYPEUSERGENERICGROUPTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LOANTYPECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `LOANCODELOANNO` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 5 | `SCHEDULENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `SCHEDULESEQNO` | INTEGER | NOT NULL | PK | primary_key |  |
| 7 | `SCHEDULEDATE` | DATE |  |  |  |  |
| 8 | `REPAYMENTDATE` | DATE |  |  |  |  |
| 9 | `SCHEDULEAMOUNT` | DECIMAL(20,0) |  |  |  |  |
| 10 | `PAIDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 11 | `REPAYMENTSEQNO` | INTEGER | NOT NULL |  |  |  |
| 12 | `BUSINESSUNITCODE` | CHAR(10) |  | FK | foreign_key |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINBUSINESSUNIT_BUSINESSUNIT` | `COMPANYCODE`, `BUSINESSUNITCODE` | [`FINBUSINESSUNIT`](../FINANCE/FINBUSINESSUNIT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINLOANPAY.COMPANYCODE = FINBUSINESSUNIT.COMPANYCODE AND FINLOANPAY.BUSINESSUNITCODE = FINBUSINESSUNIT.CODE` |
| `USERGENERICGROUP_LOANTYPE` | `LTEUGENGROUPTYPECOMPANYCODE`, `LTYPEUSERGENERICGROUPTYPECODE`, `LOANTYPECODE` | [`USERGENERICGROUP`](../CORE_MASTER/USERGENERICGROUP.md) | `USERGENGROUPTYPECOMPANYCODE`, `USERGENERICGROUPTYPECODE`, `CODE` | RESTRICT | `FINLOANPAY.LTEUGENGROUPTYPECOMPANYCODE = USERGENERICGROUP.USERGENGROUPTYPECOMPANYCODE AND FINLOANPAY.LTYPEUSERGENERICGROUPTYPECODE = USERGENERICGROUP.USERGENERICGROUPTYPECODE AND FINLOANPAY.LOANTYPECODE = USERGENERICGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINLOANPAYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.LTEUGENGROUPTYPECOMPANYCODE,
       t.LTYPEUSERGENERICGROUPTYPECODE,
       t.LOANTYPECODE,
       t.LOANCODELOANNO,
       t.SCHEDULENO,
       t.SCHEDULESEQNO,
       t.SCHEDULEDATE,
       t.REPAYMENTDATE,
       t.SCHEDULEAMOUNT,
       t.PAIDAMOUNT,
       t.REPAYMENTSEQNO
FROM   DB2ADMIN.FINLOANPAY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
