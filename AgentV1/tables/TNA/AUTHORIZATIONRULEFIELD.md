# DB2ADMIN.AUTHORIZATIONRULEFIELD

- **Module**: `TNA` (low confidence — FK neighbourhood: 2 of 2 related tables are TNA)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `TEMPLATECODE`, `LINE`, `ADENTITYNAME`, `ADNAME`, `UIXMLPATH`, `UIXMLNAME`, `UIXMLATTRIBUTE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 191317

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `TEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LINE` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ADENTITYNAME` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `ADNAME` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `UIXMLPATH` | VARCHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `UIXMLNAME` | VARCHAR(54) | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `UIXMLATTRIBUTE` | VARCHAR(120) | NOT NULL | PK FK | primary_key foreign_key |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `AUTHORIZATIONFIELDS_FIELD` | `COMPANYCODE`, `TEMPLATECODE`, `ADENTITYNAME`, `ADNAME`, `UIXMLPATH`, `UIXMLNAME`, `UIXMLATTRIBUTE` | [`AUTHORIZATIONFIELDS`](../TNA/AUTHORIZATIONFIELDS.md) | `AUTHORIZATIONTMPCOMPANYCODE`, `AUTHORIZATIONTEMPLATECODE`, `ADNAMEENTITYNAME`, `ADNAMENAME`, `UIXMLATTRIBUTEABSUIXMLPATH`, `UIXMLATTRIBUTEABSUIXMLNAME`, `UIXMLATTRIBUTENAME` | RESTRICT | `AUTHORIZATIONRULEFIELD.COMPANYCODE = AUTHORIZATIONFIELDS.AUTHORIZATIONTMPCOMPANYCODE AND AUTHORIZATIONRULEFIELD.TEMPLATECODE = AUTHORIZATIONFIELDS.AUTHORIZATIONTEMPLATECODE AND AUTHORIZATIONRULEFIELD.ADENTITYNAME = AUTHORIZATIONFIELDS.ADNAMEENTITYNAME AND AUTHORIZATIONRULEFIELD.ADNAME = AUTHORIZATIONFIELDS.ADNAMENAME AND AUTHORIZATIONRULEFIELD.UIXMLPATH = AUTHORIZATIONFIELDS.UIXMLATTRIBUTEABSUIXMLPATH AND AUTHORIZATIONRULEFIELD.UIXMLNAME = AUTHORIZATIONFIELDS.UIXMLATTRIBUTEABSUIXMLNAME AND AUTHORIZATIONRULEFIELD.UIXMLATTRIBUTE = AUTHORIZATIONFIELDS.UIXMLATTRIBUTENAME` |
| `AUTHORIZATIONRULE_FIELDS` | `COMPANYCODE`, `TEMPLATECODE`, `LINE` | [`AUTHORIZATIONRULE`](../TNA/AUTHORIZATIONRULE.md) | `AUTHORIZATIONTMPCOMPANYCODE`, `AUTHORIZATIONTEMPLATECODE`, `LINENUMBER` | RESTRICT | `AUTHORIZATIONRULEFIELD.COMPANYCODE = AUTHORIZATIONRULE.AUTHORIZATIONTMPCOMPANYCODE AND AUTHORIZATIONRULEFIELD.TEMPLATECODE = AUTHORIZATIONRULE.AUTHORIZATIONTEMPLATECODE AND AUTHORIZATIONRULEFIELD.LINE = AUTHORIZATIONRULE.LINENUMBER` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `AUTHORIZATIONRULEFIELDUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.TEMPLATECODE,
       t.LINE,
       t.ADENTITYNAME,
       t.ADNAME,
       t.UIXMLPATH,
       t.UIXMLNAME,
       t.UIXMLATTRIBUTE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.AUTHORIZATIONRULEFIELD t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
