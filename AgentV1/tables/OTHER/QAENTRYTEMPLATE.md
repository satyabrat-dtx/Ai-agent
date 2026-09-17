# DB2ADMIN.QAENTRYTEMPLATE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `DEPARTMENTCODE`, `ITMTYPECODE`, `ENTRYCODE`
- **FK degree**: referenced by 1 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 85046

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `DEPARTMENTCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `ITMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 4 | `ITMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `ENTRYCODE` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 6 | `LONGDESCRIPTION` | VARCHAR(100) | NOT NULL |  | description | Long human-readable label. |
| 7 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 8 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 9 | `SUPPLIERREQ` | INTEGER | NOT NULL |  |  |  |
| 10 | `CUSTOMERREQ` | INTEGER | NOT NULL |  |  |  |
| 11 | `CONTAINER` | INTEGER | NOT NULL |  |  |  |
| 12 | `CONTAINERELMNT` | INTEGER | NOT NULL |  |  |  |
| 13 | `ELEMENT` | INTEGER | NOT NULL |  |  |  |
| 14 | `PRODUCTIONORD` | INTEGER | NOT NULL |  |  |  |
| 15 | `WHLOT` | INTEGER | NOT NULL |  |  |  |
| 16 | `MRNNUM` | INTEGER | NOT NULL |  |  |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `QAENTRYTEMPLATE.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QAENTRYTEMPLATE.COMPANYCODE = DIVISION.COMPANYCODE AND QAENTRYTEMPLATE.DIVISIONCODE = DIVISION.CODE` |
| `ITEMTYPE_ITMTYPE` | `ITMTYPECOMPANYCODE`, `ITMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QAENTRYTEMPLATE.ITMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND QAENTRYTEMPLATE.ITMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `QAENTRYTEMPLATE_QARTEMPLATE` | [`QAREQUESTENTRY`](../CORE_MASTER/QAREQUESTENTRY.md) | `COMPANYCODE`, `DIVISIONCODE`, `DEPARTMENTCODE`, `ITYPECODE`, `QARTEMPLATEENTRYCODE` | `QAREQUESTENTRY.COMPANYCODE = QAENTRYTEMPLATE.COMPANYCODE AND QAREQUESTENTRY.DIVISIONCODE = QAENTRYTEMPLATE.DIVISIONCODE AND QAREQUESTENTRY.DEPARTMENTCODE = QAENTRYTEMPLATE.DEPARTMENTCODE AND QAREQUESTENTRY.ITYPECODE = QAENTRYTEMPLATE.ITMTYPECODE AND QAREQUESTENTRY.QARTEMPLATEENTRYCODE = QAENTRYTEMPLATE.ENTRYCODE` |

## Indexes

- `QAENTRYTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.DEPARTMENTCODE,
       t.ITMTYPECOMPANYCODE,
       t.ITMTYPECODE,
       t.ENTRYCODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.SUPPLIERREQ,
       t.CUSTOMERREQ,
       t.CONTAINER
FROM   DB2ADMIN.QAENTRYTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
