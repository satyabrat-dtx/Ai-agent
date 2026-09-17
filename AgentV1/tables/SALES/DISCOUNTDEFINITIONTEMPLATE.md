# DB2ADMIN.DISCOUNTDEFINITIONTEMPLATE

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 33
- **Primary key**: `COMPANYCODE`, `ORDERTYPE`, `DEFINITIONTYPE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 79760

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ORDERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 2 | `DEFINITIONTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 3 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `DIVISIONREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 8 | `ORDERPARTNERREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 9 | `ORDERPARTNERGROUPREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 10 | `FINANCIALORDERPARTNERREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 11 | `ORDERCATEGORYREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 12 | `AREAREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 13 | `STATISTICALGROUPREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 14 | `ORDERTEMPLATECODEREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 15 | `PAYMENTMETHODREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 16 | `AGENTREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 17 | `COLLECTIONREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 18 | `DISCOUNTCATEGORYREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 19 | `ITEMTYPEREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 20 | `ORDERITEMREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 21 | `ORDERITEMGROUPREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 22 | `QUALITYLEVELREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 23 | `LINEUSERVALUEREQUIRED` | CHAR(1) |  |  |  |  |
| 24 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 25 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 26 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 27 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 28 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 29 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 30 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 31 | `REFERENCEPARTNERREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 32 | `REFERENCEPARTNERGROUPREQUIRED` | CHAR(1) | NOT NULL |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `DISCOUNTDEFINITIONTEMPLATE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `DISCOUNTDEFINITIONTEMPLATE_TEMPLATE` | [`SALESDISCOUNTDEFINITION`](../SALES/SALESDISCOUNTDEFINITION.md) | `COMPANYCODE`, `ORDERTYPE`, `TYPE`, `TEMPLATECODE` | `SALESDISCOUNTDEFINITION.COMPANYCODE = DISCOUNTDEFINITIONTEMPLATE.COMPANYCODE AND SALESDISCOUNTDEFINITION.ORDERTYPE = DISCOUNTDEFINITIONTEMPLATE.ORDERTYPE AND SALESDISCOUNTDEFINITION.TYPE = DISCOUNTDEFINITIONTEMPLATE.DEFINITIONTYPE AND SALESDISCOUNTDEFINITION.TEMPLATECODE = DISCOUNTDEFINITIONTEMPLATE.CODE` |

## Indexes

- `DISCOUNTDEFINITIONTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ORDERTYPE,
       t.DEFINITIONTYPE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.DIVISIONREQUIRED,
       t.ORDERPARTNERREQUIRED,
       t.ORDERPARTNERGROUPREQUIRED,
       t.FINANCIALORDERPARTNERREQUIRED,
       t.ORDERCATEGORYREQUIRED
FROM   DB2ADMIN.DISCOUNTDEFINITIONTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
