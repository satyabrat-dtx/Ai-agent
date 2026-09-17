# DB2ADMIN.EPCGUTILIZATION

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `EPCGAPPLNCODE`, `EPCGLINENO`, `MRNDLTMRNHEADERMRNPREFIXCODE`, `MRNDETAILMRNHEADERCODE`, `MRNDETAILLINEID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 138338

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `EPCGAPPLNCODE` | CHAR(30) | NOT NULL | PK | primary_key |  |
| 3 | `EPCGLINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `MRNDLTMRNHEADERMRNPREFIXCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `MRNDETAILMRNHEADERCODE` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 6 | `MRNDETAILLINEID` | INTEGER | NOT NULL | PK | primary_key |  |
| 7 | `UTILIZEDQTY` | DECIMAL(15,5) |  |  |  |  |
| 8 | `CIFUTILIZEDVALUEFC` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 9 | `CIFUTILIZEDVALUEINR` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EPCGUTILIZATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.EPCGAPPLNCODE,
       t.EPCGLINENO,
       t.MRNDLTMRNHEADERMRNPREFIXCODE,
       t.MRNDETAILMRNHEADERCODE,
       t.MRNDETAILLINEID,
       t.UTILIZEDQTY,
       t.CIFUTILIZEDVALUEFC,
       t.CIFUTILIZEDVALUEINR,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.EPCGUTILIZATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
