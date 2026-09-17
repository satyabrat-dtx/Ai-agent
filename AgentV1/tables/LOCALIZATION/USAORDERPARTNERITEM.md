# DB2ADMIN.USAORDERPARTNERITEM

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'USA')
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `COMPANYCODE`, `NUMBERID`, `ORDERTYPE`, `ORDPRNCUSTOMERSUPPLIERCODE`, `ITEMTYPEAFICODE`, `SUBCODE01`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 115038

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 2 | `ORDERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 3 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `INITIALDATE` | DATE |  |  |  |  |
| 5 | `FINALDATE` | DATE |  |  |  |  |
| 6 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 7 | `ITEMTYPEAFICODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 8 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 9 | `SUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 10 | `SUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 11 | `SUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 12 | `SUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 13 | `SUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 14 | `SUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 15 | `SUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 16 | `SUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 17 | `SUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 18 | `EXTERNALITEMCODE` | CHAR(50) |  |  |  |  |
| 19 | `LONGDESCRIPTION` | VARCHAR(100) | NOT NULL |  | description | Long human-readable label. |
| 20 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 21 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 26 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `USAORDERPARTNERITEM.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `USAORDERPARTNERITEMUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.NUMBERID,
       t.ORDERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.INITIALDATE,
       t.FINALDATE,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04
FROM   DB2ADMIN.USAORDERPARTNERITEM t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
