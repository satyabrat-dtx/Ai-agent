# DB2ADMIN.FINASSIGNVOUCHERTEMPLATE

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `ORDERTYPE`, `LINETYPE`, `DOCUMENTTYPE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 99507

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `ORDERTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINETYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 4 | `DOCUMENTTYPE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `LONGDESCRIPTION` | VARCHAR(100) | NOT NULL |  | description | Long human-readable label. |
| 6 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 7 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 8 | `VOUCHERTEMPLATECODE` | CHAR(5) |  | FK | foreign_key |  |
| 9 | `VOUCHERNUMBERSELECT` | CHAR(1) |  |  |  |  |
| 10 | `VOUCHERDATESELECT` | CHAR(1) |  |  |  |  |
| 11 | `POSTINGDATESELECT` | CHAR(1) |  |  |  |  |
| 12 | `EXTERNALDATESELECT` | CHAR(1) |  |  |  |  |
| 13 | `EXTERNALNUMBERSELECT` | CHAR(1) |  |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINASSIGNVOUCHERTEMPLATE.COMPANYCODE = COMPANY.CODE` |
| `DOCUMENTTYPE_DOCUMENT` | `ORDERTYPE`, `DOCUMENTTYPE` | [`DOCUMENTTYPE`](../CORE_MASTER/DOCUMENTTYPE.md) | `ORDERTYPE`, `TYPE` | RESTRICT | `FINASSIGNVOUCHERTEMPLATE.ORDERTYPE = DOCUMENTTYPE.ORDERTYPE AND FINASSIGNVOUCHERTEMPLATE.DOCUMENTTYPE = DOCUMENTTYPE.TYPE` |
| `FINVOUCHERTEMPLATE_VOUCHERTEMPLATE` | `COMPANYCODE`, `VOUCHERTEMPLATECODE` | [`FINVOUCHERTEMPLATE`](../FINANCE/FINVOUCHERTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINASSIGNVOUCHERTEMPLATE.COMPANYCODE = FINVOUCHERTEMPLATE.COMPANYCODE AND FINASSIGNVOUCHERTEMPLATE.VOUCHERTEMPLATECODE = FINVOUCHERTEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINASSIGNVOUCHERTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ORDERTYPE,
       t.LINETYPE,
       t.DOCUMENTTYPE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.VOUCHERTEMPLATECODE,
       t.VOUCHERNUMBERSELECT,
       t.VOUCHERDATESELECT,
       t.POSTINGDATESELECT
FROM   DB2ADMIN.FINASSIGNVOUCHERTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
