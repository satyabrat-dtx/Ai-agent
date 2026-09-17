# DB2ADMIN.ADAUTHORIZATION

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `ADENTITYNAME`, `ADNAME`, `USERUSERID`, `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 62944

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ADENTITYNAME` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ADNAME` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `USERUSERID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `AUTHORIZATIONLEVEL` | CHAR(1) | NOT NULL |  |  |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ADADDITIONALDATA_AD` | `ADENTITYNAME`, `ADNAME` | [`ADADDITIONALDATA`](../CORE_MASTER/ADADDITIONALDATA.md) | `ENTITYNAME`, `NAME` | RESTRICT | `ADAUTHORIZATION.ADENTITYNAME = ADADDITIONALDATA.ENTITYNAME AND ADAUTHORIZATION.ADNAME = ADADDITIONALDATA.NAME` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ADAUTHORIZATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ADENTITYNAME,
       t.ADNAME,
       t.USERUSERID,
       t.COMPANYCODE,
       t.AUTHORIZATIONLEVEL,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ADAUTHORIZATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
