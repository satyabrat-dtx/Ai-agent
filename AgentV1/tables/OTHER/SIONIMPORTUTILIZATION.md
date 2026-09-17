# DB2ADMIN.SIONIMPORTUTILIZATION

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `ADVLICENSECODE`, `SIONADVSIONSIONCODE`, `SIONLINENO`, `MRNDLTMRNHEADERMRNPREFIXCODE`, `MRNDETAILMRNHEADERCODE`, `MRNDETAILLINEID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 146298

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `ADVLICENSECODE` | CHAR(30) | NOT NULL | PK | primary_key |  |
| 3 | `SIONADVSIONSIONCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `SIONLINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `MRNDLTMRNHEADERMRNPREFIXCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `MRNDETAILMRNHEADERCODE` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 7 | `MRNDETAILLINEID` | INTEGER | NOT NULL | PK | primary_key |  |
| 8 | `UTILIZEDQTY` | DECIMAL(15,5) |  |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SIONIMPORTUTILIZATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ADVLICENSECODE,
       t.SIONADVSIONSIONCODE,
       t.SIONLINENO,
       t.MRNDLTMRNHEADERMRNPREFIXCODE,
       t.MRNDETAILMRNHEADERCODE,
       t.MRNDETAILLINEID,
       t.UTILIZEDQTY,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.SIONIMPORTUTILIZATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
