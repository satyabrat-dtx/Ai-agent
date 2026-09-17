# DB2ADMIN.ABSEQBAUTH

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `ABSEQBABSUIXMLPATH`, `ABSEQBABSUIXMLNAME`, `ABSEQBCODE`, `USERUSERID`, `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 15748

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSEQBABSUIXMLPATH` | VARCHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ABSEQBABSUIXMLNAME` | VARCHAR(54) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ABSEQBCODE` | CHAR(30) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `USERUSERID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 4 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 5 | `USEALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSEQB_AUTHORIZATIONS` | `ABSEQBABSUIXMLPATH`, `ABSEQBABSUIXMLNAME`, `ABSEQBCODE` | [`ABSEQB`](../PLATFORM/ABSEQB.md) | `ABSUIXMLPATH`, `ABSUIXMLNAME`, `CODE` | RESTRICT | `ABSEQBAUTH.ABSEQBABSUIXMLPATH = ABSEQB.ABSUIXMLPATH AND ABSEQBAUTH.ABSEQBABSUIXMLNAME = ABSEQB.ABSUIXMLNAME AND ABSEQBAUTH.ABSEQBCODE = ABSEQB.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSEQBAUTHUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSEQBABSUIXMLPATH,
       t.ABSEQBABSUIXMLNAME,
       t.ABSEQBCODE,
       t.USERUSERID,
       t.COMPANYCODE,
       t.USEALLOWED,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.ABSEQBAUTH t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
