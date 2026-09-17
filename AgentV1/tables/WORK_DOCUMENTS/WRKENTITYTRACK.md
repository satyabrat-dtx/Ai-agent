# DB2ADMIN.WRKENTITYTRACK

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 32
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 190913

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 5 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 6 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 7 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `LOTCODE` | CHAR(35) |  |  |  |  |
| 17 | `ELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 18 | `ELEMENTCODE` | CHAR(15) |  |  |  |  |
| 19 | `BYELEMENT` | SMALLINT | NOT NULL |  |  |  |
| 20 | `LEVELNBR` | INTEGER | NOT NULL |  |  |  |
| 21 | `HERARCHYSEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 22 | `STARTINGLINE` | INTEGER | NOT NULL |  |  |  |
| 23 | `FATHERLINE` | INTEGER | NOT NULL |  |  |  |
| 24 | `ENTITYID` | INTEGER | NOT NULL |  |  |  |
| 25 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 26 | `APPEARABOVEINHIERARCHY` | SMALLINT | NOT NULL |  |  |  |
| 27 | `APPEARUNDERDIFFERENTFATHERS` | SMALLINT | NOT NULL |  |  |  |
| 28 | `APPEARUNDERDIFFSTARTINGENTITY` | SMALLINT | NOT NULL |  |  |  |
| 29 | `INDENTLEVEL` | CHAR(120) |  |  |  |  |
| 30 | `HASQUALITYDATA` | SMALLINT | NOT NULL |  |  |  |
| 31 | `HASQUALITYCERTIFICATE` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.COMPANYCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06
FROM   DB2ADMIN.WRKENTITYTRACK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
