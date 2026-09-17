# DB2ADMIN.QACERTIFICATECMTDEFINITION

- **Module**: `QUALITY` (low confidence — FK neighbourhood: 1 of 1 related tables are QUALITY)
- **Roles**: `business_data`
- **Columns**: 31
- **Primary key**: `COMPANYCODE`, `NUMBERID`
- **FK degree**: referenced by 0 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 192557

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 2 | `INITIALDATE` | DATE |  |  |  |  |
| 3 | `FINALDATE` | DATE |  |  |  |  |
| 4 | `COMMENTDEFINITIONTEMPLATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `COMMENTCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `COMMENTORDERTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 7 | `COMMENTCODE` | CHAR(12) |  | FK | foreign_key |  |
| 8 | `QUALITYCERTIFICATETEMPLATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `ORDERPARTNERTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 10 | `ORDERPARTNERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 11 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `ITEMTYPEAFICODE` | CHAR(3) |  | FK | foreign_key |  |
| 13 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 14 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 24 | `PROTOTYPEMANAGED` | SMALLINT | NOT NULL |  |  |  |
| 25 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 26 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 27 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 28 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 29 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 30 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMMENTS_COMMENT` | `COMMENTCOMPANYCODE`, `COMMENTORDERTYPE`, `COMMENTCODE` | [`COMMENTS`](../CORE_MASTER/COMMENTS.md) | `COMPANYCODE`, `ORDERTYPE`, `CODE` | RESTRICT | `QACERTIFICATECMTDEFINITION.COMMENTCOMPANYCODE = COMMENTS.COMPANYCODE AND QACERTIFICATECMTDEFINITION.COMMENTORDERTYPE = COMMENTS.ORDERTYPE AND QACERTIFICATECMTDEFINITION.COMMENTCODE = COMMENTS.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `QACERTIFICATECMTDEFINITION.COMPANYCODE = COMPANY.CODE` |
| `CUSTOMERSUPPLIERDATA_ORDERPARTNER` | `COMPANYCODE`, `ORDERPARTNERTYPE`, `ORDERPARTNERCODE` | [`CUSTOMERSUPPLIERDATA`](../CORE_MASTER/CUSTOMERSUPPLIERDATA.md) | `COMPANYCODE`, `TYPE`, `CODE` | RESTRICT | `QACERTIFICATECMTDEFINITION.COMPANYCODE = CUSTOMERSUPPLIERDATA.COMPANYCODE AND QACERTIFICATECMTDEFINITION.ORDERPARTNERTYPE = CUSTOMERSUPPLIERDATA.TYPE AND QACERTIFICATECMTDEFINITION.ORDERPARTNERCODE = CUSTOMERSUPPLIERDATA.CODE` |
| `ITEMTYPE_ITEMTYPEAFI` | `ITEMTYPEAFICOMPANYCODE`, `ITEMTYPEAFICODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QACERTIFICATECMTDEFINITION.ITEMTYPEAFICOMPANYCODE = ITEMTYPE.COMPANYCODE AND QACERTIFICATECMTDEFINITION.ITEMTYPEAFICODE = ITEMTYPE.CODE` |
| `QACERTIFICATECMTDEFTEMPLATE_COMMENTDEFINITIONTEMPLATE` | `COMPANYCODE`, `COMMENTDEFINITIONTEMPLATECODE` | [`QACERTIFICATECMTDEFTEMPLATE`](../QUALITY/QACERTIFICATECMTDEFTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QACERTIFICATECMTDEFINITION.COMPANYCODE = QACERTIFICATECMTDEFTEMPLATE.COMPANYCODE AND QACERTIFICATECMTDEFINITION.COMMENTDEFINITIONTEMPLATECODE = QACERTIFICATECMTDEFTEMPLATE.CODE` |
| `QUALITYCERTIFICATETEMPLATE_QUALITYCERTIFICATETEMPLATE` | `COMPANYCODE`, `QUALITYCERTIFICATETEMPLATECODE` | [`QUALITYCERTIFICATETEMPLATE`](../QUALITY/QUALITYCERTIFICATETEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QACERTIFICATECMTDEFINITION.COMPANYCODE = QUALITYCERTIFICATETEMPLATE.COMPANYCODE AND QACERTIFICATECMTDEFINITION.QUALITYCERTIFICATETEMPLATECODE = QUALITYCERTIFICATETEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `QACERTIFICATECMTDEFUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.NUMBERID,
       t.INITIALDATE,
       t.FINALDATE,
       t.COMMENTDEFINITIONTEMPLATECODE,
       t.COMMENTCOMPANYCODE,
       t.COMMENTORDERTYPE,
       t.COMMENTCODE,
       t.QUALITYCERTIFICATETEMPLATECODE,
       t.ORDERPARTNERTYPE,
       t.ORDERPARTNERCODE,
       t.ITEMTYPEAFICOMPANYCODE
FROM   DB2ADMIN.QACERTIFICATECMTDEFINITION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
