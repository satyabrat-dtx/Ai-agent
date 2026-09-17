# DB2ADMIN.MLFPSUTILIZATION

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `MLFPSAPPLICATIONCODE`, `MRNDLTMRNHEADERMRNPREFIXCODE`, `MRNDETAILMRNHEADERCODE`, `MRNDETAILLINEID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 140559

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `MLFPSAPPLICATIONCODE` | CHAR(12) | NOT NULL | PK | primary_key |  |
| 3 | `MRNDLTMRNHEADERMRNPREFIXCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `MRNDETAILMRNHEADERCODE` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 5 | `MRNDETAILLINEID` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `UTILIZEDAMT` | DECIMAL(15,5) |  |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `MLFPSUTILIZATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.MLFPSAPPLICATIONCODE,
       t.MRNDLTMRNHEADERMRNPREFIXCODE,
       t.MRNDETAILMRNHEADERCODE,
       t.MRNDETAILLINEID,
       t.UTILIZEDAMT,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.MLFPSUTILIZATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
