# DB2ADMIN.FINLOANOUTSTANDING

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `COMPANYCODE`, `LNOLTEUGENERICGROUPTYPECODE`, `LOANNOLOANTYPECODE`, `LOANNOLOANNO`, `FROMDATE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 225340

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `LNOLTEUGENERICGROUPTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LOANNOLOANTYPECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LOANNOLOANNO` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `FROMDATE` | DATE | NOT NULL | PK | primary_key | Inclusive start of a validity period. |
| 5 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 6 | `DISBURSEMENTDATE` | DATE |  |  |  |  |
| 7 | `DISBURSEMENTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 8 | `REPAYMENTDATE` | DATE |  |  |  |  |
| 9 | `REPAYMENTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 10 | `OUTSTANDINGAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINLOANOUTSTANDING.COMPANYCODE = COMPANY.CODE` |
| `FINLOANMASTER_LOANNO` | `COMPANYCODE`, `LNOLTEUGENERICGROUPTYPECODE`, `LOANNOLOANTYPECODE`, `LOANNOLOANNO` | [`FINLOANMASTER`](../FINANCE/FINLOANMASTER.md) | `COMPANYCODE`, `LTYPEUSERGENERICGROUPTYPECODE`, `LOANTYPECODE`, `LOANNO` | RESTRICT | `FINLOANOUTSTANDING.COMPANYCODE = FINLOANMASTER.COMPANYCODE AND FINLOANOUTSTANDING.LNOLTEUGENERICGROUPTYPECODE = FINLOANMASTER.LTYPEUSERGENERICGROUPTYPECODE AND FINLOANOUTSTANDING.LOANNOLOANTYPECODE = FINLOANMASTER.LOANTYPECODE AND FINLOANOUTSTANDING.LOANNOLOANNO = FINLOANMASTER.LOANNO` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINLOANOUTSTANDINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.LNOLTEUGENERICGROUPTYPECODE,
       t.LOANNOLOANTYPECODE,
       t.LOANNOLOANNO,
       t.FROMDATE,
       t.TODATE,
       t.DISBURSEMENTDATE,
       t.DISBURSEMENTAMOUNT,
       t.REPAYMENTDATE,
       t.REPAYMENTAMOUNT,
       t.OUTSTANDINGAMOUNT,
       t.CREATIONDATETIME
FROM   DB2ADMIN.FINLOANOUTSTANDING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
