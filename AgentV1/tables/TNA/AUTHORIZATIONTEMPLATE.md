# DB2ADMIN.AUTHORIZATIONTEMPLATE

- **Module**: `TNA` (low confidence — FK neighbourhood: 1 of 1 related tables are TNA)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 3 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 191368

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UIXMLPATH` | VARCHAR(50) | NOT NULL |  |  |  |
| 1 | `UIXML` | VARCHAR(54) | NOT NULL |  |  |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 14 | `ENTITYJNDINAME` | VARCHAR(100) |  | FK | foreign_key |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `AUTHORIZATIONTEMPLATE.COMPANYCODE = COMPANY.CODE` |
| `TNAPARENTENTITY_ENTITY` | `ENTITYJNDINAME` | [`TNAPARENTENTITY`](../TNA/TNAPARENTENTITY.md) | `JNDINAME` | RESTRICT | `AUTHORIZATIONTEMPLATE.ENTITYJNDINAME = TNAPARENTENTITY.JNDINAME` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `AUTHORIZATIONTEMPLATE_AUTHORIZATIONTEMPLATE` | [`ACTIVITYLINKEDENTITY`](../TNA/ACTIVITYLINKEDENTITY.md) | `TNADETAILTNAHEADERCOMPANYCODE`, `AUTHORIZATIONTEMPLATECODE` | `ACTIVITYLINKEDENTITY.TNADETAILTNAHEADERCOMPANYCODE = AUTHORIZATIONTEMPLATE.COMPANYCODE AND ACTIVITYLINKEDENTITY.AUTHORIZATIONTEMPLATECODE = AUTHORIZATIONTEMPLATE.CODE` |
| `AUTHORIZATIONTEMPLATE_AUTHORIZATIONFIELDS` | [`AUTHORIZATIONFIELDS`](../TNA/AUTHORIZATIONFIELDS.md) | `AUTHORIZATIONTMPCOMPANYCODE`, `AUTHORIZATIONTEMPLATECODE` | `AUTHORIZATIONFIELDS.AUTHORIZATIONTMPCOMPANYCODE = AUTHORIZATIONTEMPLATE.COMPANYCODE AND AUTHORIZATIONFIELDS.AUTHORIZATIONTEMPLATECODE = AUTHORIZATIONTEMPLATE.CODE` |
| `AUTHORIZATIONTEMPLATE_AUTHORIZATIONRULES` | [`AUTHORIZATIONRULE`](../TNA/AUTHORIZATIONRULE.md) | `AUTHORIZATIONTMPCOMPANYCODE`, `AUTHORIZATIONTEMPLATECODE` | `AUTHORIZATIONRULE.AUTHORIZATIONTMPCOMPANYCODE = AUTHORIZATIONTEMPLATE.COMPANYCODE AND AUTHORIZATIONRULE.AUTHORIZATIONTEMPLATECODE = AUTHORIZATIONTEMPLATE.CODE` |

## Indexes

- `AUTHORIZATIONTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.UIXMLPATH,
       t.UIXML,
       t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.AUTHORIZATIONTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
