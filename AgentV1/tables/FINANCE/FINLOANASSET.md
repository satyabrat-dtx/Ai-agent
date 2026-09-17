# DB2ADMIN.FINLOANASSET

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `FINLOANMASTERCOMPANYCODE`, `FINLMLTEUGENERICGROUPTYPECODE`, `FINLOANMASTERLOANTYPECODE`, `FINLOANMASTERLOANNO`, `SLNO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 229096

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINLOANMASTERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINLMLTEUGENERICGROUPTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FINLOANMASTERLOANTYPECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `FINLOANMASTERLOANNO` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SLNO` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `ASSETNAME` | CHAR(30) |  |  |  |  |
| 6 | `QUANTITY` | DECIMAL(4,0) |  |  |  |  |
| 7 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 8 | `DISBURSEMENT` | DECIMAL(18,5) |  |  |  |  |
| 9 | `DISBURSEMENTDATE` | DATE |  |  |  |  |
| 10 | `INTERESTSUBSIDY` | DECIMAL(3,0) |  |  |  |  |
| 11 | `CAPITALSUBSIDY` | DECIMAL(3,0) |  |  |  |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINLOANMASTER_LINE2` | `FINLOANMASTERCOMPANYCODE`, `FINLMLTEUGENERICGROUPTYPECODE`, `FINLOANMASTERLOANTYPECODE`, `FINLOANMASTERLOANNO` | [`FINLOANMASTER`](../FINANCE/FINLOANMASTER.md) | `COMPANYCODE`, `LTYPEUSERGENERICGROUPTYPECODE`, `LOANTYPECODE`, `LOANNO` | RESTRICT | `FINLOANASSET.FINLOANMASTERCOMPANYCODE = FINLOANMASTER.COMPANYCODE AND FINLOANASSET.FINLMLTEUGENERICGROUPTYPECODE = FINLOANMASTER.LTYPEUSERGENERICGROUPTYPECODE AND FINLOANASSET.FINLOANMASTERLOANTYPECODE = FINLOANMASTER.LOANTYPECODE AND FINLOANASSET.FINLOANMASTERLOANNO = FINLOANMASTER.LOANNO` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINLOANASSETUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINLOANMASTERCOMPANYCODE,
       t.FINLMLTEUGENERICGROUPTYPECODE,
       t.FINLOANMASTERLOANTYPECODE,
       t.FINLOANMASTERLOANNO,
       t.SLNO,
       t.ASSETNAME,
       t.QUANTITY,
       t.COST,
       t.DISBURSEMENT,
       t.DISBURSEMENTDATE,
       t.INTERESTSUBSIDY,
       t.CAPITALSUBSIDY
FROM   DB2ADMIN.FINLOANASSET t
FETCH FIRST 100 ROWS ONLY;
```
