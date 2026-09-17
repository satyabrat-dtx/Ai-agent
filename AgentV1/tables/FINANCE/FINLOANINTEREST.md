# DB2ADMIN.FINLOANINTEREST

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `FINLOANMASTERCOMPANYCODE`, `FINLMLTEUGENERICGROUPTYPECODE`, `FINLOANMASTERLOANTYPECODE`, `FINLOANMASTERLOANNO`, `FROMDATE`, `SLNO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 230480

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINLOANMASTERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINLMLTEUGENERICGROUPTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FINLOANMASTERLOANTYPECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `FINLOANMASTERLOANNO` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SLNO` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `FROMDATE` | DATE | NOT NULL | PK | primary_key | Inclusive start of a validity period. |
| 6 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 7 | `LENDINGRATE` | DECIMAL(5,2) |  |  |  |  |
| 8 | `MARGIN` | DECIMAL(5,2) |  |  |  |  |
| 9 | `INTEREST` | DECIMAL(6,2) |  |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINLOANMASTER_LINE` | `FINLOANMASTERCOMPANYCODE`, `FINLMLTEUGENERICGROUPTYPECODE`, `FINLOANMASTERLOANTYPECODE`, `FINLOANMASTERLOANNO` | [`FINLOANMASTER`](../FINANCE/FINLOANMASTER.md) | `COMPANYCODE`, `LTYPEUSERGENERICGROUPTYPECODE`, `LOANTYPECODE`, `LOANNO` | RESTRICT | `FINLOANINTEREST.FINLOANMASTERCOMPANYCODE = FINLOANMASTER.COMPANYCODE AND FINLOANINTEREST.FINLMLTEUGENERICGROUPTYPECODE = FINLOANMASTER.LTYPEUSERGENERICGROUPTYPECODE AND FINLOANINTEREST.FINLOANMASTERLOANTYPECODE = FINLOANMASTER.LOANTYPECODE AND FINLOANINTEREST.FINLOANMASTERLOANNO = FINLOANMASTER.LOANNO` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINLOANINTERESTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINLOANMASTERCOMPANYCODE,
       t.FINLMLTEUGENERICGROUPTYPECODE,
       t.FINLOANMASTERLOANTYPECODE,
       t.FINLOANMASTERLOANNO,
       t.SLNO,
       t.FROMDATE,
       t.TODATE,
       t.LENDINGRATE,
       t.MARGIN,
       t.INTEREST,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.FINLOANINTEREST t
FETCH FIRST 100 ROWS ONLY;
```
