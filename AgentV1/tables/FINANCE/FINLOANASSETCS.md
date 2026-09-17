# DB2ADMIN.FINLOANASSETCS

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `FINLOANCAPITALSRCOMPANYCODE`, `FINLCAPSRLTEUGENGROUPTYPECODE`, `FINLOANCAPITALSRLOANTYPECODE`, `FINLOANCAPITALSRCODELOANNO`, `FINLOANCAPITALSRSLNO`, `SLNO`, `ASSETSLNO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 228232

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINLOANCAPITALSRCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINLCAPSRLTEUGENGROUPTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FINLOANCAPITALSRLOANTYPECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `FINLOANCAPITALSRCODELOANNO` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `FINLOANCAPITALSRSLNO` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `SLNO` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `ASSETSLNO` | INTEGER | NOT NULL | PK | primary_key |  |
| 7 | `QUANTITY` | DECIMAL(4,0) |  |  |  |  |
| 8 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 9 | `CAPITALSUBSIDY` | DECIMAL(3,0) |  |  |  |  |
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
| `FINLOANCAPITALSR_LINE` | `FINLOANCAPITALSRCOMPANYCODE`, `FINLCAPSRLTEUGENGROUPTYPECODE`, `FINLOANCAPITALSRLOANTYPECODE`, `FINLOANCAPITALSRCODELOANNO`, `FINLOANCAPITALSRSLNO` | [`FINLOANCAPITALSR`](../FINANCE/FINLOANCAPITALSR.md) | `COMPANYCODE`, `LTYPEUSERGENERICGROUPTYPECODE`, `LOANTYPECODE`, `CODELOANNO`, `SLNO` | RESTRICT | `FINLOANASSETCS.FINLOANCAPITALSRCOMPANYCODE = FINLOANCAPITALSR.COMPANYCODE AND FINLOANASSETCS.FINLCAPSRLTEUGENGROUPTYPECODE = FINLOANCAPITALSR.LTYPEUSERGENERICGROUPTYPECODE AND FINLOANASSETCS.FINLOANCAPITALSRLOANTYPECODE = FINLOANCAPITALSR.LOANTYPECODE AND FINLOANASSETCS.FINLOANCAPITALSRCODELOANNO = FINLOANCAPITALSR.CODELOANNO AND FINLOANASSETCS.FINLOANCAPITALSRSLNO = FINLOANCAPITALSR.SLNO` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINLOANASSETCSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINLOANCAPITALSRCOMPANYCODE,
       t.FINLCAPSRLTEUGENGROUPTYPECODE,
       t.FINLOANCAPITALSRLOANTYPECODE,
       t.FINLOANCAPITALSRCODELOANNO,
       t.FINLOANCAPITALSRSLNO,
       t.SLNO,
       t.ASSETSLNO,
       t.QUANTITY,
       t.COST,
       t.CAPITALSUBSIDY,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.FINLOANASSETCS t
FETCH FIRST 100 ROWS ONLY;
```
