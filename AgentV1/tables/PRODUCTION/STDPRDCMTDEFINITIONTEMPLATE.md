# DB2ADMIN.STDPRDCMTDEFINITIONTEMPLATE

- **Module**: `PRODUCTION` (low confidence — FK neighbourhood: 1 of 1 related tables are PRODUCTION)
- **Roles**: `business_data`
- **Columns**: 34
- **Primary key**: `COMPANYCODE`, `DEFINITIONTYPE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 14129

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DEFINITIONTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 2 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `DIVISIONREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 7 | `CUSTOMERREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 8 | `PLANTREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 9 | `COLLECTIONREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 10 | `STATISTICALGROUPREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 11 | `PROJECTREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 12 | `WORKCENTERREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 13 | `OPERATIONREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 14 | `STANDARDREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 15 | `PRDRESERVATIONREQ` | CHAR(1) | NOT NULL |  |  |  |
| 16 | `PRDRESERVATIONLINKREQ` | CHAR(1) | NOT NULL |  |  |  |
| 17 | `ORDERTEMPLATEREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 18 | `RESERVATIONGROUPREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 19 | `RTGITEMREQ` | CHAR(1) | NOT NULL |  |  |  |
| 20 | `RTGCODEREQ` | CHAR(1) | NOT NULL |  |  |  |
| 21 | `BOMITEMREQ` | CHAR(1) | NOT NULL |  |  |  |
| 22 | `BOMCODEREQ` | CHAR(1) | NOT NULL |  |  |  |
| 23 | `SUFFIXREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 24 | `ITEMTYPEREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 25 | `ITEMREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 26 | `VARIANTREQUIRED` | CHAR(1) |  |  |  |  |
| 27 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 28 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 29 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 30 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 31 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 32 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 33 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `STDPRDCMTDEFINITIONTEMPLATE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `STDPRDCMTDEFINITIONTEMPLATE_TEMPLATE` | [`STDPRDCOMMENTDEFINITION`](../PRODUCTION/STDPRDCOMMENTDEFINITION.md) | `COMPANYCODE`, `DEFINITIONTYPE`, `TEMPLATECODE` | `STDPRDCOMMENTDEFINITION.COMPANYCODE = STDPRDCMTDEFINITIONTEMPLATE.COMPANYCODE AND STDPRDCOMMENTDEFINITION.DEFINITIONTYPE = STDPRDCMTDEFINITIONTEMPLATE.DEFINITIONTYPE AND STDPRDCOMMENTDEFINITION.TEMPLATECODE = STDPRDCMTDEFINITIONTEMPLATE.CODE` |

## Indexes

- `STDPRDCMTDEFTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DEFINITIONTYPE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.DIVISIONREQUIRED,
       t.CUSTOMERREQUIRED,
       t.PLANTREQUIRED,
       t.COLLECTIONREQUIRED,
       t.STATISTICALGROUPREQUIRED,
       t.PROJECTREQUIRED
FROM   DB2ADMIN.STDPRDCMTDEFINITIONTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
