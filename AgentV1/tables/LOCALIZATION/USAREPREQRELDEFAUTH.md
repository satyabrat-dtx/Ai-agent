# DB2ADMIN.USAREPREQRELDEFAUTH

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'USA')
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `USARRRELLEVELDEFFROMRELLEVEL`, `USARRRELLEVELDEFTORELLEVEL`, `USARRRELLVLDEFFALLBACKRELLVL`, `COMPANYCODE`, `USERUSERID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 115187

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `USARRRELLEVELDEFFROMRELLEVEL` | CHAR(2) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `USARRRELLEVELDEFTORELLEVEL` | CHAR(2) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `USARRRELLVLDEFFALLBACKRELLVL` | CHAR(2) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `USERUSERID` | CHAR(25) | NOT NULL | PK | primary_key |  |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `USAREPREQRELDEF_CHILDAUTH` | `USARRRELLEVELDEFFROMRELLEVEL`, `USARRRELLEVELDEFTORELLEVEL`, `USARRRELLVLDEFFALLBACKRELLVL` | [`USAREPREQRELDEF`](../LOCALIZATION/USAREPREQRELDEF.md) | `FROMRELLEVEL`, `TORELLEVEL`, `FBRELLEVEL` | RESTRICT | `USAREPREQRELDEFAUTH.USARRRELLEVELDEFFROMRELLEVEL = USAREPREQRELDEF.FROMRELLEVEL AND USAREPREQRELDEFAUTH.USARRRELLEVELDEFTORELLEVEL = USAREPREQRELDEF.TORELLEVEL AND USAREPREQRELDEFAUTH.USARRRELLVLDEFFALLBACKRELLVL = USAREPREQRELDEF.FBRELLEVEL` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `USAREPREQRELDEFAUTHUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.USARRRELLEVELDEFFROMRELLEVEL,
       t.USARRRELLEVELDEFTORELLEVEL,
       t.USARRRELLVLDEFFALLBACKRELLVL,
       t.COMPANYCODE,
       t.USERUSERID,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID
FROM   DB2ADMIN.USAREPREQRELDEFAUTH t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
