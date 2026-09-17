# DB2ADMIN.NOWEXTFUNCTIONAUTH

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `FUNUIXMLPATH`, `FUNUIXMLNAME`, `FUNCODE`, `USERUSERID`, `COMPANYCODE`
- **FK degree**: referenced by 2 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 21457

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FUNUIXMLPATH` | VARCHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FUNUIXMLNAME` | VARCHAR(54) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FUNCODE` | CHAR(2) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `USERUSERID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 4 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `NOWEXTFUNCTION_FUN` | `FUNUIXMLPATH`, `FUNUIXMLNAME`, `FUNCODE` | [`NOWEXTFUNCTION`](../OTHER/NOWEXTFUNCTION.md) | `UIXMLPATH`, `UIXMLNAME`, `CODE` | RESTRICT | `NOWEXTFUNCTIONAUTH.FUNUIXMLPATH = NOWEXTFUNCTION.UIXMLPATH AND NOWEXTFUNCTIONAUTH.FUNUIXMLNAME = NOWEXTFUNCTION.UIXMLNAME AND NOWEXTFUNCTIONAUTH.FUNCODE = NOWEXTFUNCTION.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `NOWEXTFUNCTIONAUTH_SUB` | [`NOWEXTFUNCTIONAUTHFLOW`](../OTHER/NOWEXTFUNCTIONAUTHFLOW.md) | `SUBFUNUIXMLPATH`, `SUBFUNUIXMLNAME`, `SUBFUNCODE`, `SUBUSERUSERID`, `SUBCOMPANYCODE` | `NOWEXTFUNCTIONAUTHFLOW.SUBFUNUIXMLPATH = NOWEXTFUNCTIONAUTH.FUNUIXMLPATH AND NOWEXTFUNCTIONAUTHFLOW.SUBFUNUIXMLNAME = NOWEXTFUNCTIONAUTH.FUNUIXMLNAME AND NOWEXTFUNCTIONAUTHFLOW.SUBFUNCODE = NOWEXTFUNCTIONAUTH.FUNCODE AND NOWEXTFUNCTIONAUTHFLOW.SUBUSERUSERID = NOWEXTFUNCTIONAUTH.USERUSERID AND NOWEXTFUNCTIONAUTHFLOW.SUBCOMPANYCODE = NOWEXTFUNCTIONAUTH.COMPANYCODE` |
| `NOWEXTFUNCTIONAUTH_SUBAUTH` | [`NOWEXTFUNCTIONAUTHFLOW`](../OTHER/NOWEXTFUNCTIONAUTHFLOW.md) | `NOWEXTFUNCTIONAUTHFUNUIXMLPATH`, `NOWEXTFUNCTIONAUTHFUNUIXMLNAME`, `NOWEXTFUNCTIONAUTHFUNCODE`, `NOWEXTFUNCTIONAUTHUSERUSERID`, `NOWEXTFUNCTIONAUTHCOMPANYCODE` | `NOWEXTFUNCTIONAUTHFLOW.NOWEXTFUNCTIONAUTHFUNUIXMLPATH = NOWEXTFUNCTIONAUTH.FUNUIXMLPATH AND NOWEXTFUNCTIONAUTHFLOW.NOWEXTFUNCTIONAUTHFUNUIXMLNAME = NOWEXTFUNCTIONAUTH.FUNUIXMLNAME AND NOWEXTFUNCTIONAUTHFLOW.NOWEXTFUNCTIONAUTHFUNCODE = NOWEXTFUNCTIONAUTH.FUNCODE AND NOWEXTFUNCTIONAUTHFLOW.NOWEXTFUNCTIONAUTHUSERUSERID = NOWEXTFUNCTIONAUTH.USERUSERID AND NOWEXTFUNCTIONAUTHFLOW.NOWEXTFUNCTIONAUTHCOMPANYCODE = NOWEXTFUNCTIONAUTH.COMPANYCODE` |

## Indexes

- `NOWEXTFUNCTIONAUTHUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FUNUIXMLPATH,
       t.FUNUIXMLNAME,
       t.FUNCODE,
       t.USERUSERID,
       t.COMPANYCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.NOWEXTFUNCTIONAUTH t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
