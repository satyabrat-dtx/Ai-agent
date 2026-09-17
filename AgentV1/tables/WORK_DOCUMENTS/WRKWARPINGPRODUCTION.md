# DB2ADMIN.WRKWARPINGPRODUCTION

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 131985

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `ENDSPERSECTION` | INTEGER | NOT NULL |  |  |  |
| 4 | `STARTTIME` | TIME |  |  |  |  |
| 5 | `ENDTIME` | TIME |  |  |  |  |
| 6 | `NOOFSECTIONS` | INTEGER | NOT NULL |  |  |  |
| 7 | `DEFECTCOL1` | INTEGER | NOT NULL |  |  |  |
| 8 | `DEFECTCOL2` | INTEGER | NOT NULL |  |  |  |
| 9 | `DEFECTCOL3` | INTEGER | NOT NULL |  |  |  |
| 10 | `DEFECTCOL4` | INTEGER | NOT NULL |  |  |  |
| 11 | `DEFECTCOL5` | INTEGER | NOT NULL |  |  |  |
| 12 | `DEFECTCOL6` | INTEGER | NOT NULL |  |  |  |
| 13 | `DEFECTCOL7` | INTEGER | NOT NULL |  |  |  |
| 14 | `DEFECTCOL8` | INTEGER | NOT NULL |  |  |  |
| 15 | `DEFECTCOL9` | INTEGER | NOT NULL |  |  |  |
| 16 | `DEFECTCOL10` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.LINENO,
       t.ENDSPERSECTION,
       t.STARTTIME,
       t.ENDTIME,
       t.NOOFSECTIONS,
       t.DEFECTCOL1,
       t.DEFECTCOL2,
       t.DEFECTCOL3,
       t.DEFECTCOL4,
       t.DEFECTCOL5
FROM   DB2ADMIN.WRKWARPINGPRODUCTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
