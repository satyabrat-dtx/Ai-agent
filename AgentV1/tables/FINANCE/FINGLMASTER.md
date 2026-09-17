# DB2ADMIN.FINGLMASTER

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 175330

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `BSPLFLAG` | CHAR(1) | NOT NULL |  |  |  |
| 6 | `CHARTOFACCUGENGRPTECMYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `CHARTOFACCUGENGROUPTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `CHARTOFACCOUNTCODE` | CHAR(10) |  | FK | foreign_key |  |
| 9 | `STATUS` | CHAR(1) | NOT NULL |  |  |  |
| 10 | `RECONCILATIONFLAG` | SMALLINT | NOT NULL |  |  |  |
| 11 | `BANKCASHFLAG` | CHAR(1) |  |  |  |  |
| 12 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINGLMASTER.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINGLMASTER.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `USERGENERICGROUP_CHARTOFACCOUNT` | `CHARTOFACCUGENGRPTECMYCODE`, `CHARTOFACCUGENGROUPTYPECODE`, `CHARTOFACCOUNTCODE` | [`USERGENERICGROUP`](../CORE_MASTER/USERGENERICGROUP.md) | `USERGENGROUPTYPECOMPANYCODE`, `USERGENERICGROUPTYPECODE`, `CODE` | RESTRICT | `FINGLMASTER.CHARTOFACCUGENGRPTECMYCODE = USERGENERICGROUP.USERGENGROUPTYPECOMPANYCODE AND FINGLMASTER.CHARTOFACCUGENGROUPTYPECODE = USERGENERICGROUP.USERGENERICGROUPTYPECODE AND FINGLMASTER.CHARTOFACCOUNTCODE = USERGENERICGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINGLMASTERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.BSPLFLAG,
       t.CHARTOFACCUGENGRPTECMYCODE,
       t.CHARTOFACCUGENGROUPTYPECODE,
       t.CHARTOFACCOUNTCODE,
       t.STATUS,
       t.RECONCILATIONFLAG,
       t.BANKCASHFLAG
FROM   DB2ADMIN.FINGLMASTER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
